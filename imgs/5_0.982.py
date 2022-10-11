d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.E, Orient.right, Length.long, Radius.low)
d.position_pen(0,1)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.medium)

d.end()
