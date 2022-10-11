d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(2,1)
d.curve(Direction.SE, Orient.right, Length.short, Radius.low)
d.position_pen(1,3)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.SW, Length.short)
d.position_pen(1,3)
d.straight_line(Direction.E, Length.medium)

d.end()
