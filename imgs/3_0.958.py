d = DslBezier()

d.position_pen(0,0)
d.curve(Direction.SE, Orient.right, Length.long, Radius.low)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.high)
d.position_pen(2,3)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)
d.position_pen(1,1)

d.end()
