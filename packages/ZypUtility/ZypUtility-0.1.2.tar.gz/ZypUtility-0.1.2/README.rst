des������zhangyp�Լ��Ĺ��ð���Ŀǰ�����������ÿ�ReadConfig����ȡ�����ļ�����ZypLog��log�ࣩ
--ReadConfig
----��ȡ�����ļ����������ļ���Ϣת����dict����ʽ������˵��C = conf������C['�����ļ�������']

--ZypLog
----����־���������̨�ͱ������ļ�����������
----def __init__(self, filename, level='info', when='D', back_count=3, fmt='''[ʱ��]:%(asctime)s
[�߳�]:%(thread)s
[����]:%(levelname)s
[·��]:%(pathname)s
[����]:%(funcName)s
[�к�]:%(lineno)d
[��Ϣ]:%(message)s
------------------
'''):
		"""
		:param filename: log��
		:param level: bug�ȼ�
		:param when: ʱ������λ S �롢M �֡�H Сʱ��D �졢W ���ڡ�midnight ÿ���賿
		:param back_count: log���������������������������ͻ��Զ�ɾ����
		:param fmt: log��ʽ��
		"""
----������� Logger��'filename',level='info', when='D', back_count=3��