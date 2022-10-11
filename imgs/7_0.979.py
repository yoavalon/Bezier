d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.SE, Orient.left, Length.short, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.long, Radius.low)
d.position_pen(1,1)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)

d.end()
