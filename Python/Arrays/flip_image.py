def rotate_image(image: List[List[int]]) -> List[List[int]]:
    
    print(image)
    
    #FLIP ROWS
    for i in range(0, len(image)):
        for j in range(0, int(len(image[i])/2)):
            temp = image[i][len(image[i])-1-j]
            image[i][len(image[i])-1-j] = image[i][j]
            image[i][j] = temp
            
            
    #EXHANGE COLUMNS
    for i in range(0, int(len(image)/2)):
        temp = image[i]
        image[i] = image[len(image)-1-i]
        image[len(image)-1-i] = temp
        
    print(image)
        
    return image
