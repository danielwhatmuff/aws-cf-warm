# aws-cf-warm
* A command line tool for warming AWS CloudFront Distributions by filling [CloudFront Edge Caches](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CloudFrontRegionaledgecaches.html)
* Global DNS servers taken from a subset of [public-dns.info](https://public-dns.info/) with 100% reliability rating.
![](https://raw.githubusercontent.com/danielwhatmuff/aws-cf-warm/master/logo/cloudfront-logo-fs8.png)

## Customizing
* To focus your warm on particular countries, choose reliable DNS servers from the "Public DNS Servers by country" links here [public-dns.info](https://public-dns.info/)
* Configure country code and IPs within `config/dns-servers.yml`
* Warming will run from the top down

## Using the CLI
* IMPORTANT: The CLI must be run in Docker, to avoid messing with your hosts DNS - install it here [Docker Install](https://docs.docker.com/engine/installation/) :whale2:
* Alias it to easily run from the command line

## Build the image (to use customized DNS servers)
```bash
$ git clone git@github.com:danielwhatmuff/aws-cf-warm.git && cd aws-cf-warm && docker build -t aws-cf-warm .
$ alias aws-cf-warm='docker run --rm -ti aws-cf-warm aws-cf-warm'
```

## Or you can pull the image (this will use preconfigured selection of DNS servers)
```bash
$ docker pull danielwhatmuff/aws-cf-warm
$ alias aws-cf-warm='docker run --rm -ti danielwhatmuff/aws-cf-warm aws-cf-warm'
```

## Warm your CF distribution!
```
$ aws-cf-warm -d yourapp.com -p https
```

## Warm your CF distribution using a list of file paths!
```
$ aws-cf-warm -d yourapp.com -p https -f config/myfiles.yml
```

## View options
```
$ aws-cf-warm -h
```

# Contributing / Issues
* Please fork the repo and create a PR to contribute.
* If you come across any dodgy DNS servers, please report them as an issue.
