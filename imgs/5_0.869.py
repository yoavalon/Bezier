d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.SW, Length.short)
d.position_pen(0,2)
d.curve(Direction.SE, Orient.right, Length.long, Radius.low)
d.curve(Direction.S, Orient.left, Length.short, Radius.low)
d.position_pen(0,0)

d.end()
