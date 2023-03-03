# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader
from azure.cli.command_modules.servicenetworking._help import helps  # pylint: disable=unused-import
# from azure.cli.core.profiles import ResourceType  # required when using python sdk


class ServicenetworkingCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        custom_command_type = CliCommandType(
            operations_tmpl='azure.cli.command_modules.servicenetworking.custom#{}')
        super().__init__(cli_ctx=cli_ctx,
                         # resource_type=ResourceType.XXX  # required when using python sdk
                         custom_command_type=custom_command_type)

    def load_command_table(self, args):
        from azure.cli.command_modules.servicenetworking.commands import load_command_table
        from azure.cli.core.aaz import load_aaz_command_table
        try:
            from . import aaz
        except ImportError:
            aaz = None
        if aaz:
            load_aaz_command_table(
                loader=self,
                aaz_pkg_name=aaz.__name__,
                args=args
            )
        load_command_table(self, args)
        return self.command_table

    def load_arguments(self, command):
        from azure.cli.command_modules.servicenetworking._params import load_arguments
        load_arguments(self, command)


COMMAND_LOADER_CLS = ServicenetworkingCommandsLoader
