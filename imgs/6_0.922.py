d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.SE, Length.long)
d.position_pen(2,1)
d.straight_line(Direction.SW, Length.long)
d.straight_line(Direction.S, Length.long)

d.end()
