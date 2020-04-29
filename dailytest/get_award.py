#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime: 2020/4/25 15:13
import random


def get_random_awards(rd_award_cfg_list, item_num=1):
    """
    计算从随机奖励配置中获得的奖励
    :param rd_award_cfg_list: 随机配置奖励
    :param item_num:
    奖励配置格式: [awardGroup1, awardGroup2, awardGroup3, ...]
    awardGroup格式: [award1, award2, award3, ...]
    award格式: [物品类型, 物品Id, 物品数量, 最小命中值, 最大命中值] 或
              [物品类型, 物品Id, 最小物品数量, 最大物品数量，最小命中值, 最大命中值]
    命中率 = 最大命中值 - 最小命中值 + 1 / 总命中率
    :rtype [[item_type, item_id, item_count], ...]
    """
    awards = []
    for award_group_cfg in rd_award_cfg_list:
        # 概率基数总和，可支持超过100的
        random_base = award_group_cfg[-1][-1]
        # 概率基数不能小于 100
        random_base = max(random_base, 100)
        for _ in xrange(item_num):
            odds = random.randint(1, random_base)
            for award_cfg in award_group_cfg:
                if award_cfg[-2] <= odds <= award_cfg[-1]:
                    # 获得物品
                    if len(award_cfg) == 6:
                        count = random.randint(award_cfg[2], award_cfg[3])
                    else:
                        count = award_cfg[2]
                    new_good = [award_cfg[0], award_cfg[1], count]

                    # 有相同物品则合并数量
                    for i, (item_type, item_id, count) in enumerate(awards):
                        new_good_type, new_good_id, new_good_count = new_good
                        if new_good_type == item_type and new_good_id == item_id:
                            count += new_good_count
                            awards[i] = (item_type, item_id, count)
                            break

                    # 没有相同物品则添加到获得奖励列表
                    else:
                        awards.append(new_good)
                    break
    return awards


def same_award_together(award_list):
    """
    合并奖励列表中，同种奖励
    :param award_list:
    :return:
    """
    new_award_list = list()
    # 有相同物品则合并数量
    for award in award_list:
        for i, (item_type, item_id, count) in enumerate(new_award_list):
            new_good_type, new_good_id, new_good_count = award
            if new_good_type == item_type and new_good_id == item_id:
                count += new_good_count
                new_award_list[i] = [item_type, item_id, count]
                break
        # 没有相同物品则添加到获得奖励列表
        else:
            new_award_list.append(award)
    return new_award_list


if __name__ == '__main__':
    award_cfg = [[[4,1,1,1,10],[5,26,1,11,40],[15,1,1,41,70],[15,11,1,71,100]]]
    award_list = []
    for _ in xrange(10):
        award_list += get_random_awards(award_cfg)
    print award_list
    together = same_award_together(award_list)
    print together

    rank_key = ('{app_id}:{srv_id}:AddReusableActivityRank:%s:Personal' % 'activity_id').format(srv_id=1461, app_id=1011)
    print rank_key