---
title: "Terraform in five minutes or your money back"
date: 2023-06-19T20:31:22+01:00
draft: false
---

Terraform is an IaC tool used for automating the process by which you build infrastructure in a consistent, repeatable way. Terraform projects
are written in a declarative language HCL (HashiCorp Configuration Language).

OK, enough of the sales pitch; let's get into it...

First things first, you are going too need to collect some prerequisite tools. These are;

- Terraform CLI
- An AWS (other public cloud providers are available) account and CLI tools
- A terminal and text editor

## Your first Terraform project

Terraform is written in files that have a `.tf` extension. A good starting point therefore, is to create a file called `terraform.tf`.
This file is where we will define our project dependencies or "providers" in HashiCorp lingo.

```tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.4.0"
    }

    archive = {
      source  = "hashicorp/archive"
      version = "~> 2.4.0"
    }
  }

  required_version = "~> 1.4"
}
```

The above example sets the minimum required terraform version and also defines two named dependencies that our project requires in order to
build our infrastructure. If you have spent any time working with either PHP Composer or NPM this will look pretty familiar.

Once we have defined our dependencies, we can run our first terraform command. `terraform init`. This command pulls down our dependencies which
will give us access to the provider's resources which we can now use to define our infrastructure.

## Variables

Next up, lets create a new file to store our variables. `variables.tf` is a reasonable name. As a starting point, lets create a single variable
for our default AWS region. Creating variables in terraform is as simple as the below.

```tf
variable "aws_region" {
  type        = string
  description = "The AWS region"
  default     = "eu-west-2"
}
```

Variables are a good starting point for learning terraform as they show the format of a unit of HCL quite clearly. Things do get a little more
complex than this, but not by a huge amount.

First up we define what is we are creating using the keyword `variable`. There are a number of other keywords such as `resource` and `data`
which we will see shortly.

Next up, we have the variable name. In this case `aws_region`. The body of each unit of terraform code is wrapped in curly braces much like in any
C style programming language. The properties that can be set on an object can be looked up in the Terraform docs or via your LSP autocomplete engine.
Here we just define the data type, a description of the variable and a default value (this can be overridden if needed). We can access variables
throughout our Terraform project with the keyword `var` and the variable name accessed via dot notation so for our example, we would
access our region via `var.aws_region`.

## Building resources

Moving swiftly on to the fun bit, lets create some resources. For our example, we will keep it as basic as possible and just create a lambda 
function. To do this, create a file called `main.tf` with the following content;

```tf
provider "aws" {
  region = var.aws_region
}

data "archive_file" "zipped_lambda_code" {
  type        = "zip"
  source_file = "${path.module}/function/index.py"
  output_path = "${path.module}/output/lambda.zip"
}

resource "aws_iam_role" "lambda_role" {
  name = "my_first_lambda_role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": "sts:AssumeRole",
    "Principal": {
      "Service": "lambda.amazonaws.com"
    }
  }]
}
EOF
}

resource "aws_lambda_function" "lambda_resource" {
  function_name    = "we-did-it-boys"
  filename         = data.archive_file.my_first_tf_lambda.output_path
  handler          = "index.handler"
  runtime          = "python3.8"
  role             = aws_iam_role.lambda_role.arn
  source_code_hash = data.archive_file.zipped_lambda_code.output_base64sha256
}
```

First up in here we use our previously created variable by setting it as a property against our AWS provider dependency and then move on to
defining a data block. Much like variables, data blocks start with a keyword and an id/name, the difference here is that there is also an 
identifier which takes in a resource name to use. Data blocks allow use to access external sources of data or resources in your configuration.
We can then access properties on the external source again via dot notation as can be seen in the way that the lambda block's `filename`, `role` and
`source_code_hash` properties are set.

In our example we are using our data construct to take a directory containing some simple python lambda code and zipping it up to a new directory.
We will use this in our lambda to set the property `filename` which is a required parameter on a lambda function construct. To keep this example
brief, I have stripped out anything that is not 100% necessary to deploy a simple lambda function. A real world example would require more resources
to be of much use. Of these two resources, the lambda function is the focus however, a required parameter on a lambda function is a role.
For this, we create a second resource which is an IAM role which we then attach to our lambda via a property.

## Ship it! 

Now that we have a basic example, we need to know how we deploy our infrastructure. But first, we need some ways to validate our configuration.
Fortunately, Terraform ships with some useful CLI tools to do just that. First, let's run `terraform fmt`. This takes our project files and 
applies some opinionated formatting rules against the code. I'm a big fan of consistently formatted code so this feature makes me happy. 

Next, we can run `terraform validate` this command does exactly what it says on the tin. It takes the project code and validates that 
it is syntactically valid code. A good time saver if you plan to run your configuration through a CI/CD process. Save time and money by validating your 
code locally before you push to your remote.

`terraform plan` will print out the execution and deployment plan for your defined infrastructure. This is useful for understanding your application
and the resources that will be deployed when we apply our changes.

Finally, `terraform apply` will deploy the plan's resources. Once this command runs successfully, you should be able to see your resources
in the AWS console. As we haven't applied any policy statements to our lambda role, there isn't a great deal we can actually _do_ with 
our lambda yet but from the console, you should now be able to trigger a test event against your code.

## Digging deeper

There are plenty more useful Terraform CLI commands which are beyond the scope of this post such as `terraform state` and `terraform taint`
so dig into the docs to see what is possible.

## Don't get stung

Public cloud resources can cost money. A _lot_ of money so to make sure you don't get hit with a hefty cloud bill make sure to tear down any 
unused resources once you are done with them. Terraform offers a handy command for just this purpose `terraform destroy`

## Wrapping up

Terraform is a nice and simple tool for building cloud infrastructure and is more declarative than competitors AWS CDK and Pulumi. I'm not sure 
whether I prefer Terraform over CDK yet but it is certainly more flexible, being able to be used outside of the AWS ecosystem. One thing to note
is that you will usually be deploying your terraform plan via a pipeline rather than firing off commands from your terminal YMMV but I have found 
CDK to be just as simple, if not more so to run in a pipeline than terraform.

You can find the accompanying code to this post [here](https://github.com/theoboldalex/terraform_in_5_mins)
