# Copyright (c) 2021, zerodha and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Userprofileupdate(Document):
    def on_update(self):
        user = frappe.get_doc("User", frappe.session.user)
        user.first_name = self.first_name
        if self.last_name:
            user.last_name = self.last_name
        if self.mobile_no:
            user.mobile_no = self.mobile_no
        if self.profile_picture:
            user.user_image = self.profile_picture

        user.save(ignore_permissions=True)

        frappe.get_doc({
            "doctype": "Robin Chapter Mapping",
            "chapter": self.city,
            "user": frappe.session.user
        }).save(ignore_permissions=True)
