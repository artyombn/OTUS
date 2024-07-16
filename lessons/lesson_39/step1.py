import cv2 as cv


def main():
    image_filepath = "data/cat.jpg"
    img = cv.imread(image_filepath)

    # cv.imshow("Cat Image", img)

    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # print(img)  # numpy format
    # print(type(img))

    print("Before --")
    print("shape:", img.shape)
    print("shape:", img.dtype)
    print("size:", img.size)
    print("nbytes:", img.nbytes)

    print("After --")
    print("gray shape:", img_gray.shape)
    print("gray dtype:", img_gray.dtype)
    print("gray size:", img_gray.size)
    print("gray nbytes:", img_gray.nbytes)

    cv.imwrite("data/cat-gray.jpg", img_gray)


if __name__ == "__main__":
    main()
