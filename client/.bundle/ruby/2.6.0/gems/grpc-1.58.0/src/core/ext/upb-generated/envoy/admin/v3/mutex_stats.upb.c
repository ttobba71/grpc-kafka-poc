/* This file was generated by upbc (the upb compiler) from the input
 * file:
 *
 *     envoy/admin/v3/mutex_stats.proto
 *
 * Do not edit -- your changes will be discarded when the file is
 * regenerated. */

#include <stddef.h>
#include "upb/collections/array_internal.h"
#include "upb/message/internal.h"
#include "upb/mini_table/enum_internal.h"
#include "envoy/admin/v3/mutex_stats.upb.h"
#include "udpa/annotations/status.upb.h"
#include "udpa/annotations/versioning.upb.h"

// Must be last.
#include "upb/port/def.inc"

static const upb_MiniTableField envoy_admin_v3_MutexStats__fields[3] = {
  {1, 0, 0, kUpb_NoSub, 4, kUpb_FieldMode_Scalar | (kUpb_FieldRep_8Byte << kUpb_FieldRep_Shift)},
  {2, 8, 0, kUpb_NoSub, 4, kUpb_FieldMode_Scalar | (kUpb_FieldRep_8Byte << kUpb_FieldRep_Shift)},
  {3, 16, 0, kUpb_NoSub, 4, kUpb_FieldMode_Scalar | (kUpb_FieldRep_8Byte << kUpb_FieldRep_Shift)},
};

const upb_MiniTable envoy_admin_v3_MutexStats_msg_init = {
  NULL,
  &envoy_admin_v3_MutexStats__fields[0],
  24, 3, kUpb_ExtMode_NonExtendable, 3, UPB_FASTTABLE_MASK(24), 0,
  UPB_FASTTABLE_INIT({
    {0x0000000000000000, &_upb_FastDecoder_DecodeGeneric},
    {0x000000003f000008, &upb_psv8_1bt},
    {0x000800003f000010, &upb_psv8_1bt},
    {0x001000003f000018, &upb_psv8_1bt},
  })
};

static const upb_MiniTable *messages_layout[1] = {
  &envoy_admin_v3_MutexStats_msg_init,
};

const upb_MiniTableFile envoy_admin_v3_mutex_stats_proto_upb_file_layout = {
  messages_layout,
  NULL,
  NULL,
  1,
  0,
  0,
};

#include "upb/port/undef.inc"
