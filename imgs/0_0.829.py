d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.SW, Orient.right, Length.short, Radius.low)
d.position_pen(1,2)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(2,2)
d.straight_line(Direction.NE, Length.medium)

d.end()
