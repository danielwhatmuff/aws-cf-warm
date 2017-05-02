# aws-cf-warm (WIP)
CLI for warming AWS CloudFront Distributions by filling [CloudFront Edge Caches](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CloudFrontRegionaledgecaches.html)

* Can be built into as a docker image with whale2: [Docker Install](https://docs.docker.com/engine/installation/)
* Alias it to easily run from the command line

## Build the image
```bash
$ git clone git@github.com:danielwhatmuff/aws-cf-warm.git && cd aws-cf-warm && docker build -t aws-cf-warm .
```

## Install using pip
```bash
$ pip install aws-cf-warm
```
