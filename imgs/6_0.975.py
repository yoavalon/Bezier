d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.NW, Length.medium)
d.position_pen(1,1)
d.curve(Direction.NW, Orient.left, Length.short, Radius.medium)

d.end()
