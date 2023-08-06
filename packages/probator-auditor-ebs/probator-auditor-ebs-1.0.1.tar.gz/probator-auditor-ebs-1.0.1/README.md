# probator-auditor-ebs

Please open issues in the [Probator](https://gitlab.com/probator/probator/issues/new?labels=auditor-ebs) repository

## Description

This auditor validates that EBS volumes are tagged and can be configured to take corrective action, if required.

## Configuration Options

| Option name       | Default Value             | Type      | Description                                                       |
|-------------------|---------------------------|-----------|-------------------------------------------------------------------|
| enabled           | False                     | bool      | Enable the EBS auditor                                            |
| interval          | 1440                      | int       | How often the auditor runs, in minutes                            |
| email\_subject    | Unattached EBS Volumes    | string    | Notification email subject                                        |
| ignore\_tags      | probator:ignore           | array     | A list of tags that will cause the auditor to ignore the volume   |

This project is based on the work for [Cloud Inquisitor](https://github.com/RiotGames/cloud-inquisitor) by Riot Games
