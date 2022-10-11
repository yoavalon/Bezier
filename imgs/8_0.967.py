d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.SE, Orient.right, Length.short, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(3,0)

d.end()
