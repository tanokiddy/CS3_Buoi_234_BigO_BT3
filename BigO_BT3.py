# while i < n:                          N
#
#     while a < n:                      N^2   
#         while b < n:                  N^3        
#             b = b + 1                 2N^3     
#         a = a + 1                     2N^2    
#     while c < n:                      N^2
#         c = c + 1                     2N^2    
#     i = i + 100                       2N/100    


#1: Phân tích
    #1: Đối với vòng lặp:
        # Do chưa xác định được các giá trị của i, a, b, c; vì thế rất khó xác định chính xác các số lần lặp của từng dòng, tuy nhiên khi tính độ phức tạp BigO, các hằng số sẽ bị loại bỏ, ví dụ 2N sẽ chỉ còn N, hoặc 3N^3 + 1 sẽ chỉ còn N^3, vậy nên tôi tạm loại bỏ đi các hằng số.

    #2: Đối với đệ quy:
        # Đệ quy bản chất là 1 hàm gọi lại chính nó bên trong hàm đó
        # Điều kiện dừng trong đệ quy dùng để thoát vòng lặp, nếu không có điều kiện dừng đệ quy thì nó sẽ lặp vô tận
        
    #3: Đối với thao tác khác:
        # Vì tất cả đều nằm trong vòng lặp, nên số lần lặp đã ghi chi tiết ở trên
#2: Output
    # F(N) = N + 2N/100 + N^2 + 2N^2 + N^2 + 2N^2 + N^3 + 2N^3
    # O(N^3)