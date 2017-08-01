# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


# 系表
class Department(models.Model):
    # 系编号
    # 0 错误   1 生物工程  2 生物技术  3 生物信息
    id = models.IntegerField(16, primary_key=True, default=0)
    # 系名
    name = models.CharField(max_length=16, default=u'未记录')
    # 教师总数
    teacher_sum = models.IntegerField()
    # 学生总数
    student_sun = models.IntegerField()
    # 系负责人
    leader = models.ForeignKey('User', related_name='leader')
    # 系部联系方式
    phone = models.CharField(max_length=11, default=u'未记录')

    class Meta:
        # 数据表名
        db_table = 'Department'

    def __unicode__(self):
        return str(self.id) + ' ' + self.name


# 用户表
class User(models.Model):
    # 用户名  即教工卡卡号
    id = models.CharField(max_length=16, primary_key=True)
    # 姓名
    name = models.CharField(max_length=16, default=u'未记录')
    # 职称
    title = models.CharField(max_length=16, default=u'未记录')
    # 所属系 外键
    department = models.ForeignKey(Department, related_name='department', default=0)
    # 密码 md5加密后的字符串
    password = models.CharField(max_length=32, default=u'未记录')
    # 手机号
    phone_number = models.CharField(max_length=11, default=u'未记录')
    # 邮箱
    email = models.CharField(max_length=32, default=u'未记录')
    # 身份
    STATUS_CHOICES = ('教师', '系负责人', '教务员', '系统管理员', '未记录')
    status = models.CharField(max_length=16, default=u'未记录')
    USER_VERIFY = ('通过', '未通过')

    class Meta:
        # 数据表名
        db_table = 'User'

    def __unicode__(self):
        return self.id + ' ' + self.name


class Class(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    # 姓名
    name = models.CharField(max_length=16, default=u'未记录')
    # 职称
    year = models.CharField(max_length=16, default=u'未记录')

    class Meta:
        # 数据表名
        db_table = 'Class'

    def __unicode__(self):
        return self.id + ' ' + self.name


class Course(models.Model):
    # 课程编号
    id = models.CharField(max_length=16, primary_key=True)
    # 课程名称
    name = models.CharField(max_length=32, default=u'未记录')
    # 课时数
    session = models.IntegerField(128, default=0)
    # 授课老师
    lecture = models.ForeignKey(User, related_name='lecture')
    # 是否主修
    class_name = models.ForeignKey(Class)
    MAJOR_CHOICES = ('主修', '代课')
    major = models.CharField(max_length=16, default=u'未记录')
    # 学分
    credit = models.IntegerField(16, default=0)
    people = models.IntegerField(default = 0)
    # 听课人数
    COURSE_VERIFY = ('通过', '未通过')

    class Meta:
        # 数据表名
        db_table = 'Course'

    def __unicode__(self):
        return self.id + ' ' + self.name


class Project(models.Model):
    # 课程编号
    id = models.CharField(max_length=16, primary_key=True)
    # 课程名称
    magazine = models.CharField(max_length=32, default=u'未记录')
    prize = models.CharField(max_length=32, default=u'未记录')
    title = models.CharField(max_length=32, default=u'未记录')
    # 论文题目或是项目题目
    name = models.ForeignKey(User,related_name='teacher_name')
    # 获奖老师

    # 是否主修
    class_name = models.ForeignKey(Class)
    PROJECT_VERIFY = ('通过', '未通过')


    class Meta:
        # 数据表名
        db_table = 'Project'

    def __unicode__(self):
        return self.id + ' ' + self.name