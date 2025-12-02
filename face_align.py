# shim: face alignment implementation moved into ex3.py
try:
    from ex3 import (align_face, flip_lr, get_landmarks,
                     get_shape_keypoints, get_affine_keypoints, FACE_OVAL_IDX)
except Exception as e:
    raise ImportError("face_align moved into ex3.py; import functions from ex3.py directly") from e

