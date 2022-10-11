d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(0,2)
d.curve(Direction.SW, Orient.left, Length.short, Radius.low)
d.straight_line(Direction.E, Length.medium)
d.position_pen(2,2)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.medium)

d.end()
