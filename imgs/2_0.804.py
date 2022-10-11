d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.SW, Length.short)
d.position_pen(2,3)
d.curve(Direction.SE, Orient.right, Length.short, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)
d.position_pen(0,0)

d.end()
