# Đồ án CS114: Nhận diện người điều khiển xe máy không có mũ bảo hiểm

## Pipeline:
Phát hiện người đi xe máy trong khung hình (detection) 
$\Rightarrow$ Phân loại (có mũ / không)

## Dataset:
Gồm 2 dataset:
- Cho model detection (**dataset 1**): 
    - Trong folder `bike_detect_img`.
    - Có sẵn, cần reannotation và thực hiện augmentation để tăng cường dữ liệu.
- Cho model classification: 
    - Trong folder `helmet_classify_img`.
    - Crop từ **dataset 1** và scrape trên web (link các website để scrape để trong file source.txt), thực hiện annotation & augmentation để tăng cường dữ liệu.