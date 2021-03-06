# -*- coding: utf-8 -*-
# V7.0 - Release
{
    "name": "Pentaho Email Patch",
    "version": "1.0",
    "depends": ["pentaho_reports", "email_template"],
    "author": "Richard deMeester",
    "category": "Generic Modules/Base",
    "description": """
Resolve Pentaho reports/email concurrency issue
===============================================

This works around the OpenERP user concurrency issue when generating a Pentaho report at the same time as parsing the email template.

Creates duplicate user when spawning a Pentaho report from email templates.
""",
    "data": [
             ],
    "demo": [],
    "test": [],
    "installable": True,
    "active": False,
}
