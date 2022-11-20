from rocketmq.client import Producer, Message

producer = Producer("producer")
producer.set_namesrv_addr('127.0.0.1:9876')
producer.start()

message = Message('topic-hello')
message.set_keys('key')
message.set_tags('tag')
message.set_body('{"key":"value"}')

ret = producer.send_sync(message)
print(ret.status, ret.msg_id, ret.offset)
producer.shutdown()
