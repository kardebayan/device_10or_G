#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#
from extract_utils.file import File
from extract_utils.fixups_blob import (
    BlobFixupCtx,
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)
from extract_utils.tools import (
    llvm_objdump_path,
)
from extract_utils.utils import (
    run_cmd,
)

namespace_imports = [
    'device/10or/G',
    'hardware/qcom-caf/msm8953',
    'vendor/qcom/opensource/dataservices',
    'vendor/qcom/opensource/commonsys/display',
    'vendor/qcom/opensource/display',
]

def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None
lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'com.qualcomm.qti.dpm.api@1.0',
        'vendor.qti.imsrtpservice@3.0',
    ): lib_fixup_vendor_suffix,
}

blob_fixups: blob_fixups_user_type = {
    ('vendor/lib/libubifocus.so', 'vendor/lib/libHAFIAFalSDE1.so', 'vendor/lib/libtrueportrait.so', 'vendor/lib/libmmcamera_hdr_gb_lib.so', 'vendor/lib/libAltek_AF.so', 'vendor/lib/libts_detected_face_hal.so', 'vendor/lib/libseemore.so', 'vendor/lib/libIQM_OTP_Correction.so', 'vendor/lib/libfcell.so', 'vendor/lib/libts_face_beautify_hal.so', 'vendor/lib/libalCMotion.so', 'vendor/lib/libchromaflash.so', 'vendor/lib/liboptizoom.so', 'vendor/lib/libIAFalSDE1.so', 'vendor/lib/libIQ_Match_Lib.so'): blob_fixup()
        .replace_needed('libstdc++.so', 'libstdc++_vendor.so'),
    'vendor/lib64/libvendor.goodix.hardware.fingerprint@1.0-service.so': blob_fixup()
        .remove_needed('libprotobuf-cpp-lite.so'),
    ('vendor/lib64/libgf_algo.so', 'vendor/lib64/libgf_ca.so', 'vendor/lib64/libgf_hal.so'): blob_fixup()
        .remove_needed('libstdc++.so'),
}

module = ExtractUtilsModule(
    'G',
    '10or',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
