# -*- coding: UTF-8 -*-

import bs4
import json
# !/usr/bin/python

import re
import html2text as ht  # pip install html2text
from bs4 import BeautifulSoup
import pandas as pd
html_doc = """
<div class="card_main"><div class="card_answer_con"><div class="popup_card answer_text content_text"><p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;王者荣耀HOOK模型分析</p><h1><strong><strong>1.产品概况</strong></strong></h1><p><strong><strong>产品定位</strong></strong>：基于微信、QQ社交关系链基础上的MOBA手游</p><p><strong><strong>产品数据</strong></strong>：</p><p>（1）用户规模：2017年5月的王者荣耀用户规模超两亿，渗透率高达22.3%</p><p>（2）日活月活：5月份日活跃用户达5412.8万人，月活跃用户达1.63亿，较去年12月数据增长100%</p><p>（3）使用习惯：王者荣耀用户日均使用次数为2.33次，日均使用时长为47.2分钟，而晚9点-11点是游戏高峰期</p><p><strong><strong>用户属性</strong></strong>：</p><p>年龄：20-24岁用户占比超1/4</p><p><span><img src="//cdn.sanjieke.cn/upload/image/181125/5bfa74760fae0.png/web" width="335" height="198"></span></p><p>性别：男女比例约为1：1.18</p><p><span><img src="//cdn.sanjieke.cn/upload/image/181125/5bfa748be0caf.png/web" width="318" height="106"></span></p><p><br></p><p>地域：王者荣耀用户相比全国网民分布更偏向二三线城市</p><p><span><img src="//cdn.sanjieke.cn/upload/image/181125/5bfa74a7a5243.png/web" width="544" height="111"></span></p><p><strong><strong>主要功能：</strong></strong><br></p><p><span><img src="//cdn.sanjieke.cn/upload/image/181125/5bfa74d0c1916.png/web" width="558" height="421"></span></p><h1><strong><strong>2.触发</strong></strong></h1><p>下图是HOOK模型的基本逻辑，下文会从这四个方面去分析王者荣耀怎么让用户上瘾。<br></p><p><strong><strong></strong></strong><span><img src="//cdn.sanjieke.cn/upload/image/181125/5bfa790613138.png/web" width="347" height="316"></span><strong><strong></strong></strong><br></p><h2><strong><strong>2.1外部触发</strong></strong></h2><p>定义：是指用户被外部因素唤醒，去使用APP</p><p>手段：</p><p><strong>（1）触达体系</strong></p><p><strong><strong>APP消息推送</strong></strong></p><p>分析：举个例子，节假日送英雄等福利活动，会以推送方式触达用户。英雄、钻石都是物质奖励，能够快速激发用户打开APP参与活动，重新进入游戏环节。</p><p><span><img src="//cdn.sanjieke.cn/upload/image/181125/5bfa75234c781.png/web" width="384" height="116"></span></p><p><span><img src="//cdn.sanjieke.cn/upload/image/181125/5bfa7538cc961.png/web" width="379" height="113"></span><br></p><p></p><p><strong><strong>王者荣耀官方微博、公众号</strong></strong></p><p>分析：官方微博/公众号的内容以福利活动、赛事、新版本预告内容为主，福利活动是触发用户到APP里参与活动；赛事主要是告知用户消息，吸引他们进入APP观战；新版本预告是告知用户有新玩法可以体验，让用户有期待感，等新版本真正上线时，用户会有更大的兴趣进入APP更新版本。<br></p><p><span><img src="//cdn.sanjieke.cn/upload/image/181125/5bfa755859552.png/web" width="445" height="336"></span></p><p><span><img src="//cdn.sanjieke.cn/upload/image/181125/5bfa7572800ed.png/web" width="273" height="479"></span></p><p><strong><strong>触手TV、虎牙直播和企鹅电竞等直播平台的游戏主播账号</strong></strong></p><p>分析：随着王者荣耀用户规模的扩大，诞生不少游戏KOL。用户方面，想要跟着KOL学习游戏技能、膜拜KOL的游戏攻略的内容消费需求也逐渐增多。进而游戏主播平台诞生很多王者荣耀游戏主播账号，而且粉丝数量很多都是几十万级粉丝以上。用户在看完直播后，可能会被激发去尝试玩一把的需求，从而打开APP进入游戏环节。</p><p><span><img src="//cdn.sanjieke.cn/upload/image/181125/5bfa758cbc7cd.png/web" width="388" height="357"></span></p><p><strong>（2）邀请好友</strong></p><p>王者荣耀主要是基于微信/QQ关系链的游戏玩法，5V5实时对战模式可以邀请微信好友一起组队。邀请消息发送到微信后，原本没有玩王者的用户，可能会被激发去打开APP玩游戏。</p><p><span><img src="//cdn.sanjieke.cn/upload/image/181125/5bfa75af50bf6.png/web" width="446" height="246"></span></p><h2><strong><strong>2.2内部触发</strong></strong></h2><p>定义：是指用户主动去打开APP，没有外界因素的直接干扰</p><p><strong><strong>（1）无聊，想要打发时间</strong></strong></p><p>王者荣耀游戏玩家打发时间的方式，习惯主要是打王者。极光大数据显示，2016年12月至2017年5月，王者荣耀用户日均使用时长均值为47.2分钟。打游戏消耗的时间以及游戏的趣味性，足以解闷和打发时间。</p><p><strong><strong>（2）打游戏解压，获得存在感</strong></strong></p><p>王者荣耀属于角色扮演打斗类游戏，实时对战中的厮杀，把敌人杀死后所获得的快感，是解压的绝佳方式。再加上多种及时反馈的奖励，例如金币、装备、技能获得、战果成绩排行，促使在实际生活中没有什么存在感的用户，在游戏里找到存在感。</p><p><strong><strong>（3）玩王者荣耀成为一种社交方式</strong></strong></p><p>王者荣耀主要游戏模式是5v5团队实时对战，熟人之间可以组队一起打游戏。例如午休时间，几个同事可以约游戏，游戏过程中的各种分工合作，可以增进感情；聚餐时间，好友之间可以组队对抗，争个输赢，寻找乐趣。陌生人之间打游戏之间的各种互动，例如语音交流，互送礼物，加好友等，也是一种寻找好友的途径。</p><p><strong><strong>（4）游戏账号升级</strong></strong></p><p>对游戏特别热爱的玩家，非常追求高等级的账号，用以证明自己玩游戏的能力。所以这批玩家可能每天都玩游戏练英雄，花在游戏上的时间也会比普通玩家多很多。另外等级排行榜之间的互相攀比，也是用户想要尽快升级账号的原因之一。</p><p><strong><strong>（5）想要获得奖励</strong></strong></p><p>王者荣耀的每日签到系统，每日任务系统，是外界的概念占据用户心智，促使用户每天登录APP去领取金币、钻石、铭文碎片等奖励。用户积攒一定的奖励后，可以购买更厉害的英雄，获得更高级的装备，从而增加游戏胜利的机会。</p><h1><strong><strong>3.行动</strong></strong></h1><p>福格行为模型公式为：B=MAT。B代表行为，M代表动机，A代表能力，T代表触发。意思是要满足这三个条件，人们就会做出某个具体行为。我所理解的触发，应该是上面所讲到的外部触发和内部触发。下面从动机和能力两方面剖析王者荣耀的做法。</p><h2><strong><strong>3.1动机</strong></strong></h2><p><strong><strong>（1）追求愉悦</strong></strong></p><p>人在什么时候会变得愉悦？其中有一种情况是：只要付出极小的成本，就能及时获得极大的回报。王者荣耀里只要控制遥杆和点触技能，就能把野兽杀死，把敌人干掉，然后经济噌噌地往上涨，甚至最后取得胜利，这会给玩家带来极大的愉悦感。</p><p><strong><strong>（2）释放愤怒</strong></strong></p><p>个人在玩游戏过程中，什么时候会有很大的动力去持续玩游戏？其实很多时候是每次打游戏失败之后。那种很想赢回来，释放上一局失败的愤怒、不甘心，是推动我持续玩游戏的巨大动力。因为人是趋利避害的，而避害往往比趋利来的更猛烈。</p><p><strong><strong>（3）避免尴尬</strong></strong></p><p>个人战绩在每局里排名靠后，还有段位比微信好友低很多的时候，为了避免尴尬，用户很可能会通过多玩游戏，来提高战绩，提升段位。</p><h2><strong><strong>3.2能力</strong></strong></h2><p>下面从游戏主流程、游戏过程、操作方式三个方面，分析王者荣耀是如何做到降低用户的行动门槛的。</p><p><strong><strong>主流程：</strong></strong></p><p><span><img src="//cdn.sanjieke.cn/upload/image/181125/5bfa762bbdde4.png/web" width="470" height="183"></span></p><p><br></p><p>王者荣耀在主流程上，是如何降低用户行动门槛的？下面分四点来说明：</p><p>（1）王者荣耀主流程基本有六步，而且引导用户进入游戏的目标特别清晰，默认推荐用户进入实时对战王者峡谷5V5模式。</p><p>（2）时匹配的时间一般控制在60秒以内，时间较短，不会让用户等太久；</p><p>（3）新手选择英雄时，推荐血量比较多的亚瑟去对打，降低用户选择英雄的成本；</p><p>（4）每个英雄有分路选择推荐，以避免新手用户刚进入游戏不知道往哪里跑的尴尬。</p><p><strong><strong>游戏过程：</strong></strong></p><p>时间：相比大型端游英雄联盟每局40-50分钟，王者荣耀打一局只需要10-30分钟</p><p>英雄：王者荣耀的英雄一共有87个，大多数只有三个专业技能，少部分四个技能。技能较少，容易操控。</p><p><span><img src="//cdn.sanjieke.cn/upload/image/181125/5bfa7668ba32f.png/web" width="550" height="326"></span></p><p>动作：游戏中，能提高经济的主要动作有打野、杀敌、推塔，目标较少而且在地图中非常清晰。</p><p>通用技能：除了回城和恢复，其他的十个技能是随着等级的升高，解锁对应的技能。在游戏中一般只能使用一个通用技能，比如上图中的惩击。限制技能使用，以减少用户在游戏中思</p><p>考太多。</p><p><span><img src="//cdn.sanjieke.cn/upload/image/181125/5bfa768ac15dd.png/web" width="466" height="409"></span></p><p><strong><strong>操作方式：</strong></strong></p><p>只要长按左边的遥杆就能控制方向和移动，只要点击右边的技能按钮就能释放技能，操作十分便捷。</p><h1><strong><strong>4.酬赏</strong></strong></h1><h2><strong><strong>4.1资源酬赏</strong></strong></h2><p><strong><strong>点数：</strong></strong>点数通常是游戏里用于量化用户行为，给予即时反馈的手段。王者荣耀里的点数主要分为四类：金币、钻石、铭文碎片、经验值。不同分类的点数，获取方式和作用都不是完全相同。点数的多样性对应酬赏多样性，而且每局对战获得点数具有不确定性，这就对应了酬赏的变化性。多变的酬赏能够促使用户有更大动力去玩游戏。</p><p><span><img src="//cdn.sanjieke.cn/upload/image/181125/5bfa76db75951.png/web" width="571" height="173"></span><br></p><h2><strong><strong>4.2社会酬赏</strong></strong></h2><p><strong><strong>（1）排行榜</strong></strong></p><p>微信好友之间的段位对比，如果排位靠前，就能获得游戏圈子里的优越感。</p><p><span><img src="//cdn.sanjieke.cn/upload/image/181125/5bfa77056a18a.png/web" width="354" height="355"></span></p><p><strong><strong>（2）交友</strong></strong></p><p>如果在游戏结束后，战绩比较优秀，可能会获得游戏好友的认可，从而添加你为好友。用户此时会觉得自己特别有价值。</p><p><span><img src="//cdn.sanjieke.cn/upload/image/181125/5bfa772524343.png/web" width="426" height="239"></span></p><h2><strong><strong>4.3自我实现酬赏</strong></strong></h2><p>等级的提升，段位的提升，还有所获得的英雄更厉害，装备更牛逼，其实都是想要自我实现，往上不断成长的奖赏。</p><h1><strong><strong>5.投入</strong></strong></h1><p>投入是指随着用户在产品中产生的行为越多，就会累积越多的存储价值，用户就越依赖产品，越离不开产品。例如数据、社交关系等。下面分三个方面看看王者荣耀是怎么设计投入的。</p><p><strong><strong>（1）等级累积提升</strong></strong></p><p>王者荣耀一共有30个等级。用户对战越多，获得的经验值越高，经验值积攒到一定数值可以提升等级。获得解锁新的游戏模式还有荣誉感。</p><p><span><img src="//cdn.sanjieke.cn/upload/image/181125/5bfa7770aa004.png/web" width="554" height="309"></span></p><p><strong><strong>（2）段位累积提升</strong></strong></p><p>王者荣耀一共有8个段位，分别是倔强青铜、秩序白银、荣耀黄金、尊贵铂金、永恒钻石、至尊星耀、最强王者、荣耀王者。排位赛赢得越多，段位提升得就越多，就可获得更多的荣誉感。</p><p><strong><strong>（3）成就</strong></strong></p><p>成就类似勋章，是里程碑式的总结和奖励。对战越多，成就会慢慢获得越多。</p><p><span><img src="//cdn.sanjieke.cn/upload/image/181125/5bfa7793df497.png/web" width="493" height="281"></span></p><h1>6.加载下一个触发</h1><p><strong>（1）用户在APP里持续地玩</strong></p><p>触发类型主要是内部触发，可能是上一局失败了，想要赢回来，赢得自尊；可能是连续胜利，带着成就感继续战斗升级账号。</p><p><strong>（2）用户退出APP后，再次进来玩</strong></p><p>触发类型是外部触发和内部触发相结合，这就又回到了第一个触发的环节。</p><p>用户重复玩游戏的行为，最终会形成习惯。最后促使用户每天无意识地打开APP玩游戏，这是上瘾的最高境界。</p></div></div> <div class="card_operation"><span class="tap_zan"><i></i>
                                1
                            </span> <span class="h_comment"><i></i>
                                0条评论
                            </span> <span class="assistant_comment"><i></i>
                                助教点评
                            </span></div> <div class="comment_area"><!----> <div class="assistant_box"><div class="all-comment-con"><div class="h-comment"><div class="c_box_list"><div class="c_box_li"><div class="bl_infos"><div class="bl_img"><img src="http://static.sanjieke.cn/src/common/img/dog.png"></div> <div class="bl_name"><span>
                                谢雪梅
                                <i class="assistant_icon">助教</i></span></div> <div class="bl_info"><span class="bl_time">2018-11-25 23:51</span></div></div> <div class="bl_content"><p>檬檬 这份作业很棒，如果不是老司机，那很用心的在收集资料，赞赞赞。最后一点很棒，是为数不多的能写到加载下一个触发，因为hook是一个闭环模型，所以在投入最后一个环节中，有及少数能分析到，很棒很棒，感觉是老司机啦，果断推优啦，最后一周继续加油哦！加油加油加油</p></div> <div data_homework="509059" data-teacher="190697" data-count="0" class="bl_bottom"><div data-id="0" class="like_help">有帮助
                            <span class="like_counts">(1)</span></div></div></div></div></div></div></div></div></div>
                            
                            """
text_maker = ht.HTML2Text()
text = text_maker.handle(html_doc)
md = text.split('#')



# # 创建一个BeautifulSoup解析对象
# soup = BeautifulSoup(html_doc, "html.parser", from_encoding="utf-8")
# # 获取所有的链接
# links = soup.find_all('p')
# imgs = soup.find_all('img')
# print("所有的段落")
#
#
# result = []
# for link in links:
#     print(link.name, link.get_text())
#     if link.get_text()!=' ':
#         result.append(link.get_text())
#         print(link.get_text())
#
df = pd.DataFrame(md)
df.to_csv("result6.txt", index=False, header=None)
