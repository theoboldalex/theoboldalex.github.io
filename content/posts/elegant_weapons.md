---
title: "Elegant weapons. For a more... civilised age."
date: 2022-12-11T20:27:00Z
draft: false
---

[These are your Father's parentheses. Elegant weapons. For a more... civilised age.](https://xkcd.com/297/)

I have been in a bit of a programming rut recently. While my day job is going just fine, I have grown a little tired of PHP and
tinkering with NeoVim configs can only go so far as to satisfy my urge to create.

Enter [Clojure](https://clojure.org/). The dynamic, JVM based Lisp dialect that has me smitten with programming once again.
Having worked with PHP, JavaScript, Python and Ruby, I have been looking for something a little different to re-invogorate my programming.
However, I didn't want to pick up a language that was too esoteric and without real world use cases. I  also wanted something that would be fun to learn. 
My day job consists of working with Object Oriented code, Databases and AWS and as much as I would like to deep dive into AWS, I just can't seem to
get excited to do that on my own time. Two strong contenders from the off were [Rust](https://www.rust-lang.org/) and [Go](https://go.dev/) however,
neither felt significantly different enough to really grip me and bring back the excitement and feelings of discovering the unknown that I had during 
my first forays into programming (although I must say, Rust did seem like a really nice language with a killer toolchain so who knows, maybe 
I'll be back here in a year's time waxing lyrical about the borrow checker as a fully paid up Rustacean 🦀).

And so, I decided to spend some time getting to know Clojure this weekend. As with any new language, the first thing I do once 
I have a toolchain installed and setup is implement the classic FizzBuzz (and have a tinker with the REPL if there is one available). 
This takes me right back to my initial meanderings into programming and is an algorithm so ingrained in my psyche, that it makes a perfect 
candidate program for getting a handle on the basic control structures of a language.

```clojure
(defn is_divisible_by [num divisor]
  (= 0 (mod num divisor)))

(defn fizz_buzz [start limit]
  (loop [i start]
    (when (<= i limit)
    (cond
      (is_divisible_by i 15) (println "FizzBuzz")
      (is_divisible_by i 3) (println "Fizz")
      (is_divisible_by i 5) (println "Buzz")
      :else (println i))
    (recur (inc i)))))

(fizz_buzz 1 100)
```

Although simple, the FizzBuzz problem requires the use of functions, loops and conditionals meaning some research is required to understand
the syntax and idioms of the language in order to implement it.

Once I have sucessfully implemented this simple program, I now have enough of a grasp of the language fundamentals, that I can pause and
dive into the language community a little. It is usually at this point, that I will catch some conference talks, read up on blog articles and pick through
the common packages and frameworks. I watched a few conference talks from Clojure's creator Rich Hickey which were [fantatsic](https://www.youtube.com/watch?v=rI8tNMsozo0).

Being someone that works primarily as a backend web developer, the obvious next step is to create a simple, single threaded web server. Clojure makes this 
a relatively easy and pain free process but does require at least one dependency. In order to do this, it is idiomatic to use a tool such as 
[Leiningen](https://leiningen.org/). To get started, just install Leiningen using your system's package manager

```bash
brew install leiningen
```

and once that has successfully installed, bootstrap a new Clojure project 

```bash
lein new simple_http_server
```

You should now have a directory called `simple_http_server` in your filesystem that has some boilerplate files included. It is idiomatic in Clojure to 
strap together small sets of libraries rather than using fully fledged "batteries included" frameworks and so, as we are building a web server,
we will want a library that handles http requests. I have chosen [http-kit](https://github.com/http-kit/http-kit) for this task.

In order for our project to know about http-kit, we need to add the dependency to our newly generated `project.clj` files and also define
where our main function will be.

```clojure
(defproject simple_http_server "0.1.0-SNAPSHOT"
  :author "Alex Theobold"
  :description "A simple single threaded HTTP web server"
  :min-lein-version "2.7.1"
  :license {:name "The MIT License"
            :url "http://opensource.org/licenses/MIT"}
  :dependencies [[org.clojure/clojure "1.8.0"]
                 [http-kit "2.2.0"]
                 [org.clojure/data.json "2.4.0"]
                 [jakarta.xml.bind/jakarta.xml.bind-api "2.3.2"]
                 [org.glassfish.jaxb/jaxb-runtime "2.3.2"]]
  :main simple_http_server.core)
```

Next, we write as simple a server that you are likely to find. This just returns a JSON message on GET requests to the root URI.

```clojure
(ns simple_http_server.core
  (:require [org.httpkit.server :refer [run-server]]
            [clojure.data.json :as json]))

(def port (read-string (or (System/getenv "PORT") "8000")))

(defn app [req]
  {:status  200
   :headers {"Content-Type" "application/json"}
   :body    (json/write-str {:message "Hello, World!"})})

(defn -main [& args]
  (run-server app {:port port})
  (println (str "Server listening on port " port)))
```

The code here is far from perfect and probably goes against many best practices, but that is not the aim here, the aim is to get up and 
running with something as quickly as possible so that we can iterate on it and pick up idioms and best practice by building something non-trivial.

So from here on out I will just keep the fun factor alive and build out a simple project using Clojure. Maybe I'll find a use case for it in my day
job. Maybe it will teach me to think diffrently about programming or maybe not. All I know right now is that I'm having fun programming again. 

Long may that continue.
