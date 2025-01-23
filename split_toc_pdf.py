import fitz  # PyMuPDF
import sys

def split_pdf(input_pdf, output_prefix, split_pages_list):
    """
    切分PDF文件
    input_pdf: 输入PDF文件路径
    output_prefix: 输出文件名前缀
    split_pages: 每个文件的页码范围 [(start1, end1), (start2, end2), ...]
    """
    doc = fitz.open(input_pdf)

    bookmarks = doc.get_toc(simple=True)  # 获取书签（简单模式）
    
    output_files = []
    
    for i in range(len(split_pages_list) // 2):
        start, end = int(split_pages_list[i*2]), int(split_pages_list[i*2+1])
        # 创建一个新的PDF文档
        new_doc = fitz.open()
        
        # 从原文档中提取所需页码
        for page_num in range(start-1, end):  # 页码从0开始
            new_doc.insert_pdf(doc, from_page=page_num, to_page=page_num)
        
        new_bookmarks = []
        level_diff = None
        for level, title, page_num in bookmarks:
            # 根据原始页码，调整到新的文件中
            if start <= page_num <= end:
                new_page_num = page_num - start + 1  # 调整为当前文件的页码
                if level_diff is None:
                    level_diff = level - 1
                new_bookmarks.append((level - level_diff if level >= level_diff else 1, title, new_page_num))
        
        # 添加书签
        #print(new_bookmarks)
        new_doc.set_toc(new_bookmarks)
        
        # 保存到新文件, 禁用压缩，并保留图片分辨率
        output_file = f"{output_prefix}_part_{i+1}.pdf"
        new_doc.save(output_file, garbage=4, deflate=True)  # 保留原始分辨率和图片质量
        output_files.append(output_file)
    
    return output_files


# 示例使用
def main(input_pdf, output_prefix, split_pages):
    output_files = split_pdf(input_pdf, output_prefix, split_pages)
    print("切分完成，输出文件：", output_files)

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python split_toc_pdf.py input_pdf output_prefix split_start split_end ...")
        sys.exit(0)
    main(sys.argv[1], sys.argv[2], sys.argv[3:])
