#include <opencv2/opencv.hpp>
#include <vector>

int main() {
    cv::VideoCapture cap("test_video.mp4");
    if(!cap.isOpened()) return -1;

    cv::Mat frame, hsv, mask;
    while(true) {
        cap >> frame;
        if(frame.empty()) break;

        cv::cvtColor(frame, hsv, cv::COLOR_BGR2HSV);

        cv::inRange(hsv, cv::Scalar(00, 20, 20), cv::Scalar(30, 255, 150), mask);
        cv::imshow("debug Mask", mask);

        std::vector<std::vector<cv::Point>> contours;
        cv::findContours(mask, contours, cv::RETR_EXTERNAL, cv::CHAIN_APPROX_SIMPLE);

        for (const auto& contour : contours) {
            if (cv::contourArea(contour) > 100) {
                cv::Rect bbox = cv::boundingRect(contour);
                cv::rectangle(frame, bbox, cv::Scalar(0, 255, 0), 2);
                cv::putText(frame, "Bolt Detected", cv::Point(bbox.x, bbox.y - 10), 
                            cv::FONT_HERSHEY_SIMPLEX, 0.5, cv::Scalar(0, 255, 0), 2);
            }
        }

        cv::imshow("C++ Industrial Tracker", frame);
        if(cv::waitKey(30) == 'q') break;
    }
    return 0;
}
