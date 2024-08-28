#!/usr/bin/python
import json
import os
import sys

def main(json_values, enm_artifact_number, rhel_artifact_number):
    json_dict = dict(json_values)
    product_set_list = json_dict.get("productset_drop_data")

    contents = []

    for product_set in product_set_list:
        if product_set.get("status") == "passed":
            contents = product_set.get("contents")
            break

    enm_url = ""
    rhel_patches_url = ""

    for content in contents:
        if enm_artifact_number == content.get("artifactNumber"):
            enm_url = content.get("hubUrl")

        if rhel_artifact_number == content.get("artifactNumber"):
            rhel_patches_url = content.get("hubUrl")

        if enm_url.strip() and rhel_patches_url.strip():
            enm_list = enm_url.split("/")
            index = len(enm_list) - 1
            enm_iso_name = enm_list[index]

            rhel_list = rhel_patches_url.split("/")
            index = len(rhel_list) - 1
            rhel_patches_name = rhel_list[index]

            print(enm_url)
            print(rhel_patches_url)
            print(enm_iso_name.strip("/"))
            print(rhel_patches_name.strip("/"))

            return True

    return False

if __name__ == "__main__":
    try:
        json_filename = sys.argv[1]
        enm_art_number = sys.argv[2]
        rhel_art_number = sys.argv[3]

        json_file = open(json_filename, "r+")
        json_vls = json.load(json_file)
        is_success = main(json_vls, enm_art_number, rhel_art_number)
    except Exception:
        is_success = False

    if not is_success:
        sys.exit(1)

    sys.exit()

