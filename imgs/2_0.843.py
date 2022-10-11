d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.SE, Orient.left, Length.short, Radius.low)
d.position_pen(1,3)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.SE, Orient.right, Length.short, Radius.low)

d.end()
