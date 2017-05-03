# aws-cf-warm
CLI for warming AWS CloudFront Distributions by filling [CloudFront Edge Caches](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CloudFrontRegionaledgecaches.html)
![](https://raw.githubusercontent.com/danielwhatmuff/aws-cf-warm/master/logo/cloudfront-logo-fs8.png)

* Requires Docker to run :whale2: [Docker Install](https://docs.docker.com/engine/installation/)
* Alias it to easily run from the command line

## Pull the image
```bash
$ docker pull danielwhatmuff/aws-cf-warm
$ alias aws-cf-warm='docker run --rm -ti danielwhatmuff/aws-cf-warm aws-cf-warm'
```
Add the alias to your bash_profile or bashrc.

## Build the image
```bash
$ git clone git@github.com:danielwhatmuff/aws-cf-warm.git && cd aws-cf-warm && docker build -t aws-cf-warm .
```

## Add a bash alias
```
$ alias aws-cf-warm='docker run --rm -ti aws-cf-warm aws-cf-warm'
```

### Warm your distribution!
```
$ docker run --rm -ti aws-cf-warm aws-cf-warm.py -d yourapp.com
```

# Contributing / Issues
* Please fork the repo and create a PR to contribute.
* If you come across any dodgy DNS servers, please report them as an issue.
