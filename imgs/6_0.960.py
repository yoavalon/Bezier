d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.SE, Length.long)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.position_pen(3,0)
d.curve(Direction.N, Orient.right, Length.long, Radius.medium)
d.position_pen(2,0)
d.curve(Direction.W, Orient.left, Length.short, Radius.low)
d.position_pen(0,1)

d.end()
