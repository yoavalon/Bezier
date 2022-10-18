d = DslBezier()

d.position_pen(0,0)
d.position_pen(2,2)
d.position_pen(2,2)
d.curve(Direction.W, Orient.right, Length.long, Radius.medium)
d.position_pen(1,0)

d.end()
