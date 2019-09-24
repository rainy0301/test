# -*- coding:utf-8 -*-

import numpy as np

def calcu_award_cost(p,n,r,takerate,takerate_n,award_type,award_power):
    '''
    计算各种优惠券成本
    p:本金
    n:期限
    r:年化利率
    takerate:费用
    takerate_n:费用分数
    award_type:奖券类型 支持：利息，费用，息费
    award_power:优惠力度，int(>=1)：几期免息，float(<1)：折扣比例; 如 1 ：1期免息；0.9：利息9折
    '''
    # pmt = np.pmt(r/12,n,-p)  # 每期本息
    per = np.arange(n) + 1
    ipmt = np.ipmt(r/12,per,n,-p)  # 每期利息
    interest = sum(ipmt)           # 利息总和

    fees = p * takerate  # 费用
    per_fees = fees / takerate_n # 每期费用

    if award_power > n:
        print('注意：优惠力度大于期限')
        return '注意：优惠力度大于期限'

    # 利息券
    if award_type == '利息':
        # 几期免息
        if award_power >= 1:
            free_is = ipmt[:award_power]
            return round(sum(free_is),4), round(sum(free_is)/p,4)
        # 整体利息折扣券
        else:
            free_is = interest * (1-award_power)
            return round(free_is,4), round(free_is/p,4)
    elif award_type == '费用':
        # 几期免息
        if award_power >= 1:
            if award_power > takerate_n:
                return '免费期数超过费用分期数'
            free_is = per_fees * award_power
            return round(free_is,4), round(free_is/p,4)
        # 整体利息折扣券
        else:
            free_is = fees * (1-award_power)
            return round(free_is,4), round(free_is/p,4)

    elif award_type == '息费':
        # 几期免息
        if award_power >= 1:
            free_is = ipmt[:award_power] # 利息
            if award_power > takerate_n:
                free_fees = fees
            else:
                free_fees = per_fees * award_power  # 费用
            return round(sum(free_is) + free_fees, 4) , round((sum(free_is) + free_fees)/p,4)
        # 整体利息折扣券
        else:
            free_is = (interest+fees) * (1-award_power)            
            return round(free_is,4), round(free_is/p,4)

    else:
        print('请输入正确的优惠券类型，目前支持：利息，费用，息费三种类型')

if __name__ == "__main__":
    print('函数测试')

    p = 20000  # 本金
    n = 6     # 期限
    r = 0.12  # 年利率
    takerate = 0.04  # 费用率
    takerate_n = 6   # 费用分期数
    award_type = '息费'   # 优惠券类型
    award_power = 0.85     # 优惠力度
    print(f'本金：{p}；期限：{n}；利率：{r}；费用率：{takerate}; 费用分期数：{takerate_n}; 优惠券类型：{award_type}; 优惠券力度:{award_power}')
    cost, cost_rt = calcu_award_cost(p,n,r,takerate,takerate_n,award_type,award_power)
    print(f'成本：{cost}, 成本占本金比例：{cost_rt}')