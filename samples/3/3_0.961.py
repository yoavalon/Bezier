d = DslBezier()

d.position_pen(2,3)
d.position_pen(3,2)
d.position_pen(1,2)
d.straight_line(Direction.SE, Length.long)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(2,1)
d.position_pen(2,0)
d.position_pen(1,0)
d.position_pen(2,1)

d.end()
