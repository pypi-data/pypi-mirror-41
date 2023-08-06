# probator-auditor-iam

Please open issues in the [Probator](https://gitlab.com/probator/probator/issues/new?labels=auditor-iam) repository


## Description

This auditor validates and applies IAM policies for AWS Accounts.

## Configuration Options

| Option name               | Default Value | Type      | Description                                                               |
|---------------------------|---------------|-----------|---------------------------------------------------------------------------|
| enabled                   | `False`       | bool      | Enable the IAM roles and auditor                                          |
| interval                  | `30`          | int       | How often the auditor executes, in minutes                                |
| manage\_roles             | `True`        | bool      | Enable management of IAM roles                                            |
| roles                     | `True`        | string    | JSON document with roles to push to accounts. See below for example       |
| delete\_inline\_policies  | `False`       | bool      | Delete inline policies from existing roles                                |
| hostname                  | *None*        | string    | Git server hostname                                                       |
| repository                | *None*        | string    | Path of the Git repository                                                |
| authentication_type       | `oauth-token` | string    | Authentication type                                                       |
| oauth_token               | *None*        | string    | OAuth2 token. Required if `authentication_type` is `oauth-token`          |
| username                  | *None*        | string    | Git username. Required if `authentication_type` is `username-password`    |
| password                  | *None*        | string    | Git password./Required if `authentication_type` is `username-password`    |
| max_session_duration      | `8`           | string    | IAM Assume Role MaxSessionDuration (in hours)                             |
| disable\_ssl\_verify      | `False`       | bool      | Disable SSL certificate validation                                        |


### `roles` configuration

The `roles` setting allows you to configure roles to create and manage on all accounts enabled in Probator. The JSON document is structured as
a dictionary, with the top-level key being the name of the role, and the dictionary value has two keys; `trust` and `policies`

#### `trust`

The `trust` setting must be a valid IAM Assume Role Policy Document. If the `trust` key is an empty object (`{}`), null or not set, the default trust
document is provided.

#### `policies`

The `policies` key contains a list of IAM policy names to attach to the role. These policies must exist within the account before running the auditor,
ideally being created by the auditor as well.

#### Example document

The example below shows how one can manage the role probator assumes for monitoring and auditing in your accounts

```json
{
    "probator_role": {
        "trust": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "",
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": "arn:aws:iam::123456789012:role/probator-instance-role",
                        "Service": "ec2.amazonaws.com"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        },
        "policies": [
            "ProbatorAccess"
        ]
    }
}
```

This project is based on the work for [Cloud Inquisitor](https://github.com/RiotGames/cloud-inquisitor) by Riot Games
