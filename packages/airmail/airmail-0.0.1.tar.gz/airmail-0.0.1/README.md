# Airmail

> A CLI tool for deploying projects to AWS

## Introduction/Philosophy

The point of Airmail is to make deploying projects into AWS a little easier. It was inspired as a binding layer between [Terraformed](https://www.terraform.io/) infrastructure and deploying applications to [AWS ECS](https://docs.aws.amazon.com/ecs/index.html). At NYMag we wanted to manage infrastructure with Terraform and then allow applications to be more declarative about how they run without caring about the infrastructure. A developer should be able to change easily declare where and how their application will run and then be able to easily configure resources in Terraform to support that. Airmail is designed to deploy code _with the assumption that the underlying infrastructure is there to support the project_.

## How To

Airmail needs to be run in a project with a `.deploy` directory. It will look inside this directory for configuration files that will tell the tool how to deploy to ECS.

    .
    ├── ...
    ├── .deploy                 # The directory holding the config
    │   ├── config.yml          # Holds the primary config declarations
    │   └── <env>.env           # Environment variable configuration for the container
    └── ...

### Config File
[Config file docs coming soon](./docs/config.md)


## Local Development

Currently configured to use `watchcode` for re-building: https://github.com/bluenote10/watchcode
