#
# Copyright (C) 2021-2023 The PixelOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/non_ab_device.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/product_launched_with_n_mr1.mk)

# Inherit from G device
AB_OTA_UPDATER := false
$(call inherit-product, device/10or/G/device.mk)

# Inherit some common LineageOS stuff
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

# Boot Animation
TARGET_BOOT_ANIMATION_RES := 1080

# Device identifier. This must come after all inclusions.
PRODUCT_BRAND := 10.or
PRODUCT_DEVICE := G
PRODUCT_MANUFACTURER := 10.or
PRODUCT_NAME := lineage_G
PRODUCT_MODEL := 10.or G

PRODUCT_GMS_CLIENTID_BASE := android-huaqin
TARGET_VENDOR := 10.or

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="G-user 8.1.0 OPM1.171019.019 10or_G_V1_0_82 release-keys" \
    BuildFingerprint=10or/G/G:8.1.0/OPM1.171019.019/10or_G_V1_0_82:user/release-keys
