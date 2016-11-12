
# aqt - AWS Query Tool
A command-line tool for extracting information from AWS.

`aqt` simplifies issuing basic but routine queries.

## Usage
Call `aqt` by providing some credential information followed by a `select x where y` clause. The `y` component is a series of n filters of the format `filter value`. Multiple filters look like `filter-a value-a filter-b value-b`.

Currently, only EC2 instance queries is supported.

In the example below, the AWS CLI profile `my-profile` is used for authentication. The rest of the invocation says to `select`the `PrivateIpAddress` property from all EC2 instances `where` a tag with the key `Cluster` has a value of `my-cluster` and a tag of `Role` has a value of `master`.
```
aqt --profile my-profile \
    select PrivateIpAddress \
    where tag:Cluster my-cluster tag:Role master
10.10.10.120
10.10.10.210
10.10.10.94
```

## Installation
Installation can be accomplished many ways for those familiar with python packages. The recommended method is:
```
git clone https://bitbucket.org/credomobile/tools-aqt.git
cd aqt
make && make install
```

## License
MIT
