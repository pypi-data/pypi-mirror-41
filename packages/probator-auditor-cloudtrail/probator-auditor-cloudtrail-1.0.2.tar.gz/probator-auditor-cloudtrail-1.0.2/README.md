# probator-auditor-cloudtrail

Please open issues in the [Probator](https://gitlab.com/probator/probator/issues/new?labels=auditor-cloudtrail) repository

## Description

This auditor ensures that CloudTrail:

* Is enabled globally on multi-region
* Logs to a central location
* Has SNS/SQS notifications enabled and being sent to the correct queues
* Regional trails (of our chosen name) are not enabled

## Configuration Options

| Option name           | Default Value | Type      | Description                                                               |
|-----------------------|---------------|-----------|---------------------------------------------------------------------------|
| enabled               | False         | bool      | Enable the CloudTrail auditor                                             |
| interval              | 60            | int       | Run frequency in minutes                                                  |
| bucket\_account       | *None*        | string    | Name of the S3 bucket to send CloudTrail logs to                          |
| bucket\_name          | *None*        | string    | Name of account to create the S3 bucket in                                |
| bucket\_region        | us-west-2     | string    | Region to create S3 bucket in                                             |
| cloudtrail\_region    | us-west-2     | string    | Region to create CloudTrail in                                            |
| sns\_topic\_name      | *None*        | string    | SNS topic name for CloudTrail log delivery                                |
| sqs\_queue\_account   | *None*        | string    | Name of account of SQS queue for CloudTrail log delivery notifications    |
| sqs\_queue\_name      | *None*        | string    | SQS queue name                                                            |
| sqs\_queue\_region    | us-west-2     | string    | Region for the SQS queue                                                  |
| trail\_name           | us-west-2     | string    | Name of the trail to create                                               |


Based on the work by Riot Games' [Cloud Inquisitor](https://github.com/RiotGames/cloud-inquisitor)
