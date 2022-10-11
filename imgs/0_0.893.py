d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)
d.position_pen(1,2)
d.straight_line(Direction.SE, Length.short)
d.position_pen(1,1)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.low)

d.end()
