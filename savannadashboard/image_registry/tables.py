# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright (c) 2013 Mirantis Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

from django import template
from django.utils.translation import ugettext_lazy as _

from horizon import tables

LOG = logging.getLogger(__name__)


class EditTagsAction(tables.LinkAction):
    name = "edit_tags"
    verbose_name = _("Edit tags")
    url = "horizon:savanna:image_registry:edit_tags"
    classes = ("ajax-modal", "btn-create")


def tags_to_string(image):
    template_name = 'image_registry/_list_tags.html'
    context = {"image": image}
    return template.loader.render_to_string(template_name, context)


class ImageRegistryTable(tables.DataTable):
    name = tables.Column("name",
                         verbose_name=_("Image name"))
    #type = tables.Column("type",
    #                     verbose_name=_("Type"))
    tags = tables.Column(tags_to_string,
                         verbose_name=_("Tags"))

    class Meta:
        name = "image_registry"
        verbose_name = _("Image registry")
        table_actions = ()
        row_actions = (EditTagsAction,)