#SPDX-License-Identifier: BSD-3-Clause

'''
views.py

(C) Copyright 2020 Friedrich Luetze GmbH, S. Strobel, S. Hentges <lsd@luetze.de>
'''
from django.shortcuts import render
from tools.models import Tool


def tools_list(request):
    """
    Renders a list of used tools.
    """
    tools_temp_list = []
    for tool in Tool.objects.all():
        if tool.title not in tools_temp_list:
            tools_temp_list.append(tool.title)

    context = {"tools": tools_temp_list}
    return render(request, "tools/tools_list.html", context)


def tool_version_list(request, tool_name):
    """
    Renders a list of used tools with a specific name.
    """
    tools_temp_list = Tool.objects.order_by("-date_posted").filter(title=tool_name)
    context = {"tools": tools_temp_list}
    return render(request, "tools/tool_version_list.html", context)


def tool_details(request, tool_name, tool_version):
    """
    Renders a single tool, choosen through tool name and version number.
    """
    context = {
        "tool": Tool.objects.order_by("-date_posted").filter(
            title=tool_name, version=tool_version
        )[0]
    }
    return render(request, "tools/tool_details.html", context)
