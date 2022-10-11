d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.E, Length.short)
d.position_pen(2,2)
d.curve(Direction.W, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)

d.end()
