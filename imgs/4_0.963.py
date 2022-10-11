d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(2,1)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.SE, Orient.left, Length.short, Radius.high)

d.end()
