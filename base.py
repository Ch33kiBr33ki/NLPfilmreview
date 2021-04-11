import requests;

def get_content(id, page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    cookies = {'cookie': 'bid=GOOb4vXwNcc; douban-fav-remind=1; ps=y; ue="maplekonghou@163.com"; push_noty_num=0; push_doumail_num=0; ap=1; ll="108288"; dbcl2="181095881:BSb6IVAXxCI"; ck=Fd1S; ct=y'}
    url = "https://movie.douban.com/subject/" + str(id) + "/comments?start=" + str(page * 10) + "&limit=20&sort=new_score&status=P"
    res = requests.get(url, headers=headers, cookies=cookies)
    for i in range(1, 21):   # 每页20个评论用户
        name = x.xpath('//*[@id="comments"]/div[{}]/div[2]/h3/span[2]/a/text()'.format(i))
        # 下面是个大bug，如果有的人没有评分，但是评论了，那么score解析出来是日期，而日期所在位置spen[3]为空
        score = x.xpath('//*[@id="comments"]/div[{}]/div[2]/h3/span[2]/span[2]/@title'.format(i))
        date = x.xpath('//*[@id="comments"]/div[{}]/div[2]/h3/span[2]/span[3]/@title'.format(i))
        m = '\d{4}-\d{2}-\d{2}'
        try:
            match = re.compile(m).match(score[0])
        except IndexError:
            break
        if match is not None:
            date = score
            score = ["null"]
        else:
            pass
        content = x.xpath('//*[@id="comments"]/div[{}]/div[2]/p/span/text()'.format(i))
        id = x.xpath('//*[@id="comments"]/div[{}]/div[2]/h3/span[2]/a/@href'.format(i))
        try:
            city = get_city(id[0], i)  # 调用评论用户的ID城市信息获取
        except IndexError:
            city = " "
        name_list.append(str(name[0]))
        score_list.append(str(score[0]).strip('[]\''))  # bug 有些人评论了文字，但是没有给出评分
        date_list.append(str(date[0]).strip('[\'').split(' ')[0])
        content_list.append(str(content[0]).strip())
        city_list.append(city)