import cv2


# def create_video_from_frames(frame_paths, output_video_path, fps=10):
#     try:
#         frame_size = None
#         out = None
#         frame_number = 0  # Initialize frame number
#
#         fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#
#         for frame_path in frame_paths:
#             img = cv2.imread(frame_path[0])
#
#             if frame_size is None:
#                 frame_size = (img.shape[1], img.shape[0])
#                 out = cv2.VideoWriter(output_video_path, fourcc, fps, frame_size)
#
#             # Add frame number label onto the frame
#             label = f'Frame: {frame_number}'
#             cv2.putText(img, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
#
#             out.write(img)
#             frame_number += 1  # Increment frame number
#
#         if out is not None:
#             out.release()
#
#         return True, output_video_path
#
#     except Exception as e:
#         print(e)
#         return False, None

def create_video_from_frames(frame_generator, output_video_path, fps=10):

    for frame in frame_generator:
        frame_size = None
        out = None
        frame_number = 0  # Initialize frame number

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')

        img = frame.frame

        if frame_size is None:
            frame_size = (img.shape[1], img.shape[0])
            out = cv2.VideoWriter(output_video_path, fourcc, fps, frame_size)

        # Add frame number label onto the frame
        label = f'Frame: {frame_number}'
        cv2.putText(img, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        out.write(img)
        frame_number += 1  # Increment frame number

    if out is not None:
        out.release()

    return True, output_video_path
