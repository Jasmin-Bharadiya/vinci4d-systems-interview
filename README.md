# systems-interview

## Overview
This problem centers around deploying machine learning models. There are three parts. We start from a trained model that needs to be built into a service. Then that service needs to be packaged and deployed. Finally, we need to design an architecture for deploying this model into a customer's infrastructure.

The models might simulate physics, encode certain shapes and geometries in a latent space, or extract answers to questions about an engineering requirements document. We can consider this one in particular to be a geometry encoder model whose outputs inform a recommendation system for generative engineering design. The recommendations would be served to the user via a web app.

## Part 1: Model serving
We would like you to take a pretrained model and prepare it for serving. You can use any model serving framework you'd like, or write your own using a web server framework like FastAPI.

You'll get a repo that has the following files relevant for this part:
- A requirements.txt
- A client.py which, when run, will ping the model server with an example input and print the result of a correctness test (pass or fail)
- A skeleton server.py which contains functions to load the model and make a prediction
- A model.pkl which contains the pretrained model

Running server.py to bring up the server should produce no errors, and then running client.py should output a success message. We estimate this takes 30-45 minutes.

## Part 2: Package and build
We want to deploy this model to multiple environments by packaging it as a Docker container.

The provided repo contains these files for this part of the project:
- A mostly-empty Dockerfile
- An empty build.sh
- An empty deploy.sh

The following things should work:
- Running build.sh should execute the container build step
- Running deploy.sh should bring up the container as a server like in the last section
- As before, running client.py should ping the container from outside and produce a success message

We expect this might take 45 minutes to an hour. Docker is a fiddly thing, feel free to email us questions if you get stuck.

## Part 3: System architecture and deployment
Now, imagine you’re working with us to deploy this model to a customer. The customer requires this to be on their infrastructure behind a firewall. We’d like to get information about the model's performance back to our systems for monitoring operations and improving the model.

We'd like you to write a spec for how we might accomplish this. Write it in Markdown in `architecture.md`.

A few things to focus on:
- What are the most important design considerations and open questions to guide decision making?
- What general system architecture would you employ here? Defend your choices and discuss tradeoffs.
- What technology supports the proposed architecture?
- What is the operational story? Consider a bug reported by the customer: what is the process for understanding, fixing, and redeploying?

Imagine you're in week 1 of this project. You don't have to be super detailed on everything, prefer less volume and more high-quality thinking. We just want to see how you approach this type of problem from a clean sheet.

We'd recommend allocating 2 hours for this portion.
