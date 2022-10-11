d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(2,2)
d.curve(Direction.NW, Orient.left, Length.short, Radius.medium)
d.position_pen(2,0)

d.end()
