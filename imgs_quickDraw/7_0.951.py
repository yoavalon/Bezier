d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.SW, Length.long)
d.straight_line(Direction.SE, Length.long)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.N, Length.short)
d.position_pen(2,2)
d.straight_line(Direction.S, Length.long)

d.end()
