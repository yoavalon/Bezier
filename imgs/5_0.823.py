d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.SW, Length.short)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.low)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.SW, Length.medium)

d.end()
